# InsertStackedBalloon Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertStackedBalloon`

Obsolete. Superseded by IModelDocExtension::InsertStackedBalloon.
Obsolete. Superseded by [IModelDocExtension::InsertStackedBalloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertStackedBalloon( _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String _
) As Note
```

```

Dim instance As IModelDoc2
Dim Style As System.Integer
Dim Size As System.Integer
Dim UpperTextStyle As System.Integer
Dim UpperText As System.String
Dim LowerTextStyle As System.Integer
Dim LowerText As System.String
Dim value As Note
 
value = instance.InsertStackedBalloon(Style, Size, UpperTextStyle, UpperText, LowerTextStyle, LowerText)
```

```

Note InsertStackedBalloon( 
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText
)
```

```

Note^ InsertStackedBalloon( 
   System.int Style,
   System.int Size,
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText
) 
```

#### Parameters

*Style*
:   Balloon style as defined in [swBalloonStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html)

*Size*
:   Balloon size as defined in [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html)

*UpperTextStyle*
:   Text style for the upper text of the balloon as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html)

*UpperText*
:   Text in the balloon

*LowerTextStyle*
:   Text style for the lower text of the balloon as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html)

*LowerText*
:   Text in the lower part of the balloon when Style = swBS\_SplitCirc

#### Return Value

Newly created [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

This method adds a single balloon note attached to the pre-selected entity. The note is located near the pre-selection.

This method returns a Note object, which you can then use to access the note; for example, setting the font of the note text or setting the position of the Note. You can stack notes on the Note object returned by this method.

Use [INote::GetBalloonStack](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.md) with this note to get the [IBalloonStack](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.md) object. You can control various properties of the stack, such as the direction and size. You can also use the BalloonStack to stack more balloons on this first balloon.

If the balloon style is split circle, both the lower- and upper-text arguments are used. If the balloon style is anything other than split circle, the upper-text arguments are used and the lower-text arguments are ignored.

If the text style is item number or quantity, the note text is determined through the pres-selected entity to which this note is attached and the corresponding text argument is ignored. If the pre-selection is just a location on the drawing, not an entity, then the text style should be custom and you must specify the text to use.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[INote::IsStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloon.md)  
[INote::IsStackedBalloonMaster Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloonMaster.md)
