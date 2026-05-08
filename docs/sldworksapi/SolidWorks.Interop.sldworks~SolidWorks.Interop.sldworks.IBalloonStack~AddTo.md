# AddTo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~AddTo`

Adds a balloon note to this balloon stack.
Adds a balloon note to this balloon stack.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddTo( _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String _
) As Note
```

```

Dim instance As IBalloonStack
Dim UpperTextStyle As System.Integer
Dim UpperText As System.String
Dim LowerTextStyle As System.Integer
Dim LowerText As System.String
Dim value As Note
 
value = instance.AddTo(UpperTextStyle, UpperText, LowerTextStyle, LowerText)
```

```

Note AddTo( 
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText
)
```

```

Note^ AddTo( 
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText
) 
```

#### Parameters

*UpperTextStyle*
:   Text style for the text of the balloon as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html)

*UpperText*
:   Text in the balloon

*LowerTextStyle*
:   Text style for the text of the balloon as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html)

*LowerText*
:   Text in the lower part of the balloon (when Style = swBS\_SplitCirc)

#### Return Value

[INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

This method adds a balloon note that is attached to the preselected entity to this stack. It returns an INote object, which you can then use to access the note (for example, to set the font of the note text). The balloon style and size are the same as the initial balloon in this stack.

If the balloon style is split circle, this method uses both the lower and upper text arguments. If the balloon style is anything other than split circle, this method uses the upper text arguments and ignores the lower text arguments.

If the text style is item number or quantity, SOLIDWORKS uses the note text to determine the preselected entity that this note is attached to, and ignores the corresponding text argument. If the preselection is a location on the drawing instead of an entity, you must specify the text style and text.

Use [INote::GetBalloonStack](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.md) to get a balloon stack interface from an existing note.

Example

[Add Balloon to Stacked Balloon (C#)](Add_Balloon_to_Stacked_Balloon_Example_CSharp.htm)  
[Add Balloon to Stacked Balloon (VB.NET)](Add_Balloon_to_Stacked_Balloon_Example_VBNET.htm)  
[Add Balloon to Stacked Balloon (VBA)](Add_Balloon_to_Stacked_Balloon_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.md)  
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.md)  
[INote::MakeStackedBalloon Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~MakeStackedBalloon.md)
