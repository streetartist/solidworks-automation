# InsertBOMBalloon Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon`

Obsolete. Superseded by IModelDocExtension::InsertBomBalloon2.
Obsolete. Superseded by [IModelDocExtension::InsertBomBalloon2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertBOMBalloon( _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String, _
   ByVal CustomSize As System.Double, _
   ByVal ShowQuantity As System.Boolean, _
   ByVal QuantityPlacement As System.Short, _
   ByVal QuantityDenotationText As System.String _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Style As System.Integer
Dim Size As System.Integer
Dim UpperTextStyle As System.Integer
Dim UpperText As System.String
Dim LowerTextStyle As System.Integer
Dim LowerText As System.String
Dim CustomSize As System.Double
Dim ShowQuantity As System.Boolean
Dim QuantityPlacement As System.Short
Dim QuantityDenotationText As System.String
Dim value As System.Object
 
value = instance.InsertBOMBalloon(Style, Size, UpperTextStyle, UpperText, LowerTextStyle, LowerText, CustomSize, ShowQuantity, QuantityPlacement, QuantityDenotationText)
```

```

System.object InsertBOMBalloon( 
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText,
   System.double CustomSize,
   System.bool ShowQuantity,
   System.short QuantityPlacement,
   System.string QuantityDenotationText
)
```

```

System.Object^ InsertBOMBalloon( 
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText,
   System.double CustomSize,
   System.bool ShowQuantity,
   System.short QuantityPlacement,
   System.String^ QuantityDenotationText
) 
```

#### Parameters

*Style*
:   Balloon style as defined in [swBalloonStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html)

*Size*
:   Balloon size as defined in [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html)

*UpperTextStyle*
:   Style for the upper text of the balloon as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html) (see **Remarks**)

*UpperText*
:   Upper text of the balloon

*LowerTextStyle*
:   Style for the lower text of the balloon as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/Solidworks.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html); valid for balloons only and Style must be set to swBS\_SplitCirc (see **Remarks**)

*LowerText*
:   Lower text of the balloon; valid for balloons only and Style must be set to swBS\_SplitCirc

*CustomSize*
:   :   User-defined size of the balloon; Size must be set to swBF\_UserDef

*ShowQuantity*
:   :   True to show quantity, false to not

*QuantityPlacement*
:   Placement of quantity value:

    - 0 = Left
    - 1 = Right
    - 2 = Top
    - 3 = Bottom

*QuantityDenotationText*
:   Denotation text for quantity

#### Return Value

[Note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

See [INote::PropertyLinkedText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.md) for examples of link strings usable with swBalloonTextContent\_e.swBalloonTextCustomProperties.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IDrawingDoc::AutoBalloon3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon3.md)  
[INote::GetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.md)  
[INote::GetBomBalloonTextStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonTextStyle.md)  
[INote::SetBomBalloonText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.md)  
[INote::IsBomBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBomBalloon.md)
