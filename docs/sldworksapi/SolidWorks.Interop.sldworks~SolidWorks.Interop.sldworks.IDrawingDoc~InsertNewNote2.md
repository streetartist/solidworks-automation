# InsertNewNote2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2`

Creates a new note in this drawing.
Creates a new note in this drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertNewNote2( _
   ByVal UpperText As System.String, _
   ByVal LowerText As System.String, _
   ByVal NoLeader As System.Boolean, _
   ByVal BentLeader As System.Boolean, _
   ByVal ArrowStyle As System.Short, _
   ByVal LeaderSide As System.Short, _
   ByVal Angle As System.Double, _
   ByVal BalloonStyle As System.Short, _
   ByVal BalloonFit As System.Short, _
   ByVal UpperNoteContent As System.Short, _
   ByVal LowerNoteContent As System.Short _
) 
```

```

Dim instance As IDrawingDoc
Dim UpperText As System.String
Dim LowerText As System.String
Dim NoLeader As System.Boolean
Dim BentLeader As System.Boolean
Dim ArrowStyle As System.Short
Dim LeaderSide As System.Short
Dim Angle As System.Double
Dim BalloonStyle As System.Short
Dim BalloonFit As System.Short
Dim UpperNoteContent As System.Short
Dim LowerNoteContent As System.Short
 
instance.InsertNewNote2(UpperText, LowerText, NoLeader, BentLeader, ArrowStyle, LeaderSide, Angle, BalloonStyle, BalloonFit, UpperNoteContent, LowerNoteContent)
```

```

void InsertNewNote2( 
   System.string UpperText,
   System.string LowerText,
   System.bool NoLeader,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide,
   System.double Angle,
   System.short BalloonStyle,
   System.short BalloonFit,
   System.short UpperNoteContent,
   System.short LowerNoteContent
)
```

```

void InsertNewNote2( 
   System.String^ UpperText,
   System.String^ LowerText,
   System.bool NoLeader,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide,
   System.double Angle,
   System.short BalloonStyle,
   System.short BalloonFit,
   System.short UpperNoteContent,
   System.short LowerNoteContent
) 
```

#### Parameters

*UpperText*
:   Upper text string to be put in the note

*LowerText*
:   Unused; pass an empty string

*NoLeader*
:   True does not add a leader line, false does

*BentLeader*
:   True adds a bent leader line, false does not

*ArrowStyle*
:   Arrowhead type as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

*LeaderSide*
:   Leader line side as defined in [swLeaderSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html)

*Angle*
:   Text angle

*BalloonStyle*
:   Balloon style type as defined in [swBalloonStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html)

*BalloonFit*
:   Balloon fit type as defined in [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html)

*UpperNoteContent*
:   Unused; set to 0

*LowerNoteContent*
:   Unused; set to 0

Example

Contact SOLIDWORKS API Support to obtain **Insert Note Leader at Sketch Point (VBA, VB.NET, and C#)**.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::CreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCompoundNote.md)  
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.md)  
[IDrawingDoc::ICreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCompoundNote.md)  
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.md)  
[IDrawingDoc::NewNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewNote.md)  
[IDrawingDoc::InsertRevisionSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol.md)  
[IDrawingDoc::InsertCircularNotePattern Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCircularNotePattern.md)  
[IDrawingDoc::InsertLinearNotePattern Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertLinearNotePattern.md)
