# -*- coding: utf-8 -*-
from tests import FreshersTest, doc

class StylesTest(FreshersTest):
    """
    Test Resources/Styles.xml is parsed correctly
    """
    
    def setUp(self):
        super(StylesTest, self).setUp()
        self.styles = doc.get_children('Styles')[0]
    
    def test_Styles(self):
        self.assertElement(self.styles, 'Styles',
            DOMVersion="6.0"
        )
    
    def test_get_style(self):
        self.assertEqual(
            self.styles.get_style('ParagraphStyle/TV first paragraph').Self,
            self.styles.get_children('RootParagraphStyleGroup')[0].children[2].Self,
        )
    
    def test_RootCharacterStyleGroup(self):
        self.assertElement(self.styles.children[0], 'RootCharacterStyleGroup',
            Self="uad9"
        )
        self.assertEqual(len(self.styles.children[0].children), 15)
    
    def test_CharacterStyle(self):
        group = self.styles.children[0]
        self.assertElement(group.children[0], 'CharacterStyle',
            Self="CharacterStyle/$ID/[No character style]",
            Imported=False,
            Name="$ID/[No character style]"
        )
        self.assertElement(group.children[1], 'CharacterStyle',
            Self="CharacterStyle/TV drop cap",
            Imported=False,
            KeyboardShortcut=[0, 0],
            Name="TV drop cap",
            FillColor="Color/TV"
        )
        self.assertProps(group.children[1].Properties,
            BasedOn="CharacterStyle/Drop cap",
            PreviewColor="Nothing"
        )
        self.assertElement(group.children[6], 'CharacterStyle',
            Self="CharacterStyle/Drop cap",
            Imported=False,
            KeyboardShortcut=[0, 0],
            Name="Drop cap",
            FontStyle="Display"
        )
        self.assertProps(group.children[6].Properties,
            BasedOn="$ID/[No character style]",
            PreviewColor="Nothing",
            AppliedFont="Arno Pro"
        )
    
    def test_RootParagraphStyleGroup(self):
        self.assertElement(self.styles.children[1], 'RootParagraphStyleGroup',
            Self="uad7"
        )
        self.assertEqual(len(self.styles.children[1].children), 29)
    
    def test_ParagraphStyle(self):
        group = self.styles.children[1]
        self.assertElement(group.children[0], 'ParagraphStyle',
            Self="ParagraphStyle/$ID/[No paragraph style]",
            Name="$ID/[No paragraph style]",
            Imported=False,
            FillColor="Color/Black",
            FontStyle="Regular",
            PointSize=12,
            HorizontalScale=100,
            KerningMethod="$ID/Metrics",
            Ligatures=True,
            PageNumberType="AutoPageNumber",
            StrokeWeight=1,
            Tracking=0,
            Composer="HL Composer",
            DropCapCharacters=0,
            DropCapLines=0,
            BaselineShift=0,
            Capitalization="Normal",
            StrokeColor="Swatch/None",
            HyphenateLadderLimit=3,
            VerticalScale=100,
            LeftIndent=0,
            RightIndent=0,
            FirstLineIndent=0,
            AutoLeading=120,
            AppliedLanguage="$ID/English: UK",
            Hyphenation=True,
            HyphenateAfterFirst=2,
            HyphenateBeforeLast=2,
            HyphenateCapitalizedWords=True,
            HyphenateWordsLongerThan=5,
            NoBreak=False,
            HyphenationZone=36,
            SpaceBefore=0,
            SpaceAfter=0,
            Underline=False,
            OTFFigureStyle="Default",
            DesiredWordSpacing=100,
            MaximumWordSpacing=133,
            MinimumWordSpacing=80,
            DesiredLetterSpacing=0,
            MaximumLetterSpacing=0,
            MinimumLetterSpacing=0,
            DesiredGlyphScaling=100,
            MaximumGlyphScaling=100,
            MinimumGlyphScaling=100,
            StartParagraph="Anywhere",
            KeepAllLinesTogether=False,
            KeepWithNext=0,
            KeepFirstLines=2,
            KeepLastLines=2,
            Position="Normal",
            StrikeThru=False,
            CharacterAlignment="AlignEmCenter",
            KeepLinesTogether=False,
            StrokeTint=-1,
            FillTint=-1,
            OverprintStroke=False,
            OverprintFill=False,
            GradientStrokeAngle=0,
            GradientFillAngle=0,
            GradientStrokeLength=-1,
            GradientFillLength=-1,
            GradientStrokeStart=[0, 0],
            GradientFillStart=[0, 0],
            Skew=0,
            RuleAboveLineWeight=1,
            RuleAboveTint=-1,
            RuleAboveOffset=0,
            RuleAboveLeftIndent=0,
            RuleAboveRightIndent=0,
            RuleAboveWidth="ColumnWidth",
            RuleBelowLineWeight=1,
            RuleBelowTint=-1,
            RuleBelowOffset=0,
            RuleBelowLeftIndent=0,
            RuleBelowRightIndent=0,
            RuleBelowWidth="ColumnWidth",
            RuleAboveOverprint=False,
            RuleBelowOverprint=False,
            RuleAbove=False,
            RuleBelow=False,
            LastLineIndent=0,
            HyphenateLastWord=True,
            ParagraphBreakType="Anywhere",
            SingleWordJustification="FullyJustified",
            OTFOrdinal=False,
            OTFFraction=False,
            OTFDiscretionaryLigature=False,
            OTFTitling=False,
            RuleAboveGapTint=-1,
            RuleAboveGapOverprint=False,
            RuleBelowGapTint=-1,
            RuleBelowGapOverprint=False,
            Justification="LeftAlign",
            DropcapDetail=0,
            PositionalForm="None",
            OTFMark=True,
            HyphenWeight=5,
            OTFLocale=True,
            HyphenateAcrossColumns=True,
            KeepRuleAboveInFrame=False,
            IgnoreEdgeAlignment=False,
            OTFSlashedZero=False,
            OTFStylisticSets=0,
            OTFHistorical=False,
            OTFContextualAlternate=True,
            UnderlineGapOverprint=False,
            UnderlineGapTint=-1,
            UnderlineOffset=-9999,
            UnderlineOverprint=False,
            UnderlineTint=-1,
            UnderlineWeight=-9999,
            StrikeThroughGapOverprint=False,
            StrikeThroughGapTint=-1,
            StrikeThroughOffset=-9999,
            StrikeThroughOverprint=False,
            StrikeThroughTint=-1,
            StrikeThroughWeight=-9999,
            MiterLimit=4,
            StrokeAlignment="OutsideAlignment",
            EndJoin="MiterEndJoin",
            OTFSwash=False,
            Tsume=0,
            LeadingAki=-1,
            TrailingAki=-1,
            KinsokuType="KinsokuPushInFirst",
            KinsokuHangType="None",
            BunriKinshi=True,
            RubyOpenTypePro=True,
            RubyFontSize=-1,
            RubyAlignment="RubyJIS",
            RubyType="PerCharacterRuby",
            RubyParentSpacing="RubyParent121Aki",
            RubyXScale=100,
            RubyYScale=100,
            RubyXOffset=0,
            RubyYOffset=0,
            RubyPosition="AboveRight",
            RubyAutoAlign=True,
            RubyParentOverhangAmount="RubyOverhangOneRuby",
            RubyOverhang=False,
            RubyAutoScaling=False,
            RubyParentScalingPercent=66,
            RubyTint=-1,
            RubyOverprintFill="Auto",
            RubyStrokeTint=-1,
            RubyOverprintStroke="Auto",
            RubyWeight=-1,
            KentenKind="None",
            KentenFontSize=-1,
            KentenXScale=100,
            KentenYScale=100,
            KentenPlacement=0,
            KentenAlignment="AlignKentenCenter",
            KentenPosition="AboveRight",
            KentenCustomCharacter="",
            KentenCharacterSet="CharacterInput",
            KentenTint=-1,
            KentenOverprintFill="Auto",
            KentenStrokeTint=-1,
            KentenOverprintStroke="Auto",
            KentenWeight=-1,
            Tatechuyoko=False,
            TatechuyokoXOffset=0,
            TatechuyokoYOffset=0,
            AutoTcy=0,
            AutoTcyIncludeRoman=False,
            Jidori=0,
            GridGyoudori=0,
            GridAlignFirstLineOnly=False,
            GridAlignment="None",
            CharacterRotation=0,
            RotateSingleByteCharacters=False,
            Rensuuji=True,
            ShataiMagnification=0,
            ShataiDegreeAngle=4500,
            ShataiAdjustTsume=True,
            ShataiAdjustRotation=False,
            Warichu=False,
            WarichuLines=2,
            WarichuSize=50,
            WarichuLineSpacing=0,
            WarichuAlignment="Auto",
            WarichuCharsBeforeBreak=2,
            WarichuCharsAfterBreak=2,
            OTFHVKana=False,
            OTFProportionalMetrics=False,
            OTFRomanItalics=False,
            LeadingModel="LeadingModelAkiBelow",
            ScaleAffectsLineHeight=False,
            ParagraphGyoudori=False,
            CjkGridTracking=False,
            GlyphForm="None",
            RubyAutoTcyDigits=0,
            RubyAutoTcyIncludeRoman=False,
            RubyAutoTcyAutoScale=True,
            TreatIdeographicSpaceAsSpace=False,
            AllowArbitraryHyphenation=False,
            BulletsAndNumberingListType="NoList",
            NumberingStartAt=1,
            NumberingLevel=1,
            NumberingContinue=True,
            NumberingApplyRestartPolicy=True,
            BulletsAlignment="LeftAlign",
            NumberingAlignment="LeftAlign",
            NumberingExpression="^#.^t",
            BulletsTextAfter="^t",
            DigitsType="DefaultDigits",
            Kashidas="DefaultKashidas",
            DiacriticPosition="OpentypePosition",
            CharacterDirection="DefaultDirection",
            ParagraphDirection="LeftToRightDirection",
            ParagraphJustification="DefaultJustification",
            XOffsetDiacritic=0,
            YOffsetDiacritic=0,
            OTFOverlapSwash=False,
            OTFStylisticAlternate=False,
            OTFJustificationAlternate=False,
            OTFStretchedAlternate=False,
            KeyboardDirection="DefaultDirection"
        )
        self.assertProps(group.children[0].Properties,
            Leading="Auto",
            AppliedFont="Times New Roman",
            RuleAboveColor="Text Color",
            RuleBelowColor="Text Color",
            RuleAboveType="StrokeStyle/$ID/Solid",
            RuleBelowType="StrokeStyle/$ID/Solid",
            BalanceRaggedLines="NoBalancing",
            RuleAboveGapColor="Swatch/None",
            RuleBelowGapColor="Swatch/None",
            UnderlineColor="Text Color",
            UnderlineGapColor="Swatch/None",
            UnderlineType="StrokeStyle/$ID/Solid",
            StrikeThroughColor="Text Color",
            StrikeThroughGapColor="Swatch/None",
            StrikeThroughType="StrokeStyle/$ID/Solid",
            Mojikumi="Nothing",
            KinsokuSet="Nothing",
            RubyFont="$ID/",
            RubyFontStyle="Nothing",
            RubyFill="Text Color",
            RubyStroke="Text Color",
            KentenFont="$ID/",
            KentenFontStyle="Nothing",
            KentenFillColor="Text Color",
            KentenStrokeColor="Text Color",
            NumberingFormat="1, 2, 3, 4...",
            BulletsFont="$ID/",
            BulletsFontStyle="Nothing",
            AppliedNumberingList="NumberingList/$ID/[Default]",
            BulletsCharacterStyle="CharacterStyle/$ID/[No character style]",
            NumberingCharacterStyle="CharacterStyle/$ID/[No character style]",
        )
        self.assertElement(
            group.children[0].Properties.BulletChar,
            'BulletChar',
            BulletCharacterType="UnicodeOnly",
            BulletCharacterValue=8226
        )
        self.assertElement(
            group.children[0].Properties.NumberingRestartPolicies,
            'NumberingRestartPolicies',
            RestartPolicy="AnyPreviousLevel",
            LowerLevel=0,
            UpperLevel=0
        )
    
    def test_RootObjectStyleGroup(self):
        element = self.styles.get_children('RootObjectStyleGroup')[0]
        self.assertElement(
            element, 
            'RootObjectStyleGroup',
            Self="ub15"
        )
        self.assertEqual(len(element.children), 22)
        
    def test_ObjectStyle(self):
        element = self.styles.get_children('RootObjectStyleGroup')[0].children[0]
        self.assertElement(element, 'ObjectStyle',
            Self="ObjectStyle/$ID/[None]",
            Name="$ID/[None]",
            AppliedParagraphStyle="ParagraphStyle/$ID/[No paragraph style]",
            FillColor="Swatch/None",
            FillTint=-1,
            StrokeWeight=0,
            MiterLimit=4,
            EndCap="ButtEndCap",
            EndJoin="MiterEndJoin",
            StrokeType="StrokeStyle/$ID/Solid",
            LeftLineEnd="None",
            RightLineEnd="None",
            StrokeColor="Swatch/None",
            StrokeTint=-1,
            CornerRadius=12,
            GapColor="Swatch/None",
            GapTint=-1,
            StrokeAlignment="CenterAlignment",
            Nonprinting=False,
            GradientFillAngle=0,
            GradientStrokeAngle=0,
            AppliedNamedGrid="n",
            CornerOption="None"
        )
        
