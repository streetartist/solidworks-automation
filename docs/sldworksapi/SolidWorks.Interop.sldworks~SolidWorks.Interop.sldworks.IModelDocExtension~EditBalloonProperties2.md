# EditBalloonProperties2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditBalloonProperties2`

Edits the selected balloon's properties.
Edits the selected balloon's properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditBalloonProperties2( _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String, _
   ByVal CustomSize As System.Double, _
   ByVal ShowQuantity As System.Boolean, _
   ByVal QuantityPlacement As System.Short, _
   ByVal QuantityDenotationText As System.String, _
   ByVal QuantityDistance As System.Double _
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
Dim QuantityDistance As System.Double
Dim value As System.Object
 
value = instance.EditBalloonProperties2(Style, Size, UpperTextStyle, UpperText, LowerTextStyle, LowerText, CustomSize, ShowQuantity, QuantityPlacement, QuantityDenotationText, QuantityDistance)
```

```

System.object EditBalloonProperties2( 
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText,
   System.double CustomSize,
   System.bool ShowQuantity,
   System.short QuantityPlacement,
   System.string QuantityDenotationText,
   System.double QuantityDistance
)
```

```

System.Object^ EditBalloonProperties2( 
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText,
   System.double CustomSize,
   System.bool ShowQuantity,
   System.short QuantityPlacement,
   System.String^ QuantityDenotationText,
   System.double QuantityDistance
) 
```

#### Parameters

*Style*
:   Style of balloon as defined in [swBalloonStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html)

*Size*
:   Balloon size as defined in [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html)

*UpperTextStyle*
:   Balloon text style as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html)

*UpperText*
:   Text for the balloon; valid only if UpperTextStyle is one of the following:

    - swBalloonTextContent\_e.swBalloonTextCustom
    - swBalloonTextContent\_e.swBalloonTextCustomProperties
    - swBalloonTextContent\_e.swBalloonTextCutListProperties

*LowerTextStyle*
:   Lower text style as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html); valid only if Style is swBalloonStyle\_e.swBS\_SplitCirc

*LowerText*
:   Text for the lower text in the balloon; valid only if Style is swBalloonStyle\_e.swBS\_SplitCirc and LowerTextStyle is one of the following:

    - swBalloonTextContent\_e.swBalloonTextCustom
    - swBalloonTextContent\_e.swBalloonTextCustomProperties
    - swBalloonTextContent\_e.swBalloonTextCutListProperties

*CustomSize*
:   User-defined size of the balloon; valid only if Size is swBalloonFit\_e.swBF\_UserDef

*ShowQuantity*
:   True to show quantity, false to not

*QuantityPlacement*
:   Placement of quantity value as defined in [swBalloonQuantityPlacement\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonQuantityPlacement_e.html); valid only if ShowQuantity is true

*QuantityDenotationText*
:   Denotation text for quantity; valid only if ShowQuantity is true

*QuantityDistance*
:   Distance between the balloon and the quantity; valid only if ShowQuantity is true

#### Return Value

[Note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

Before calling this method, select the balloon annotation whose properties you want to edit.

Example

[Edit Balloon (VBA)](Edit_Balloon_Example_VB.htm)  
[Edit Balloon (VB.NET)](Edit_Balloon_Example_VBNET.htm)  
[Edit Balloon (C#)](Edit_Balloon_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[INote::SetBalloon Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.md)  
[INote::SetBomBalloonText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.md)
