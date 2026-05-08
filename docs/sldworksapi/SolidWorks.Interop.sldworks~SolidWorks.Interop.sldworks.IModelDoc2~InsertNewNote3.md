# InsertNewNote3 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNewNote3`

Creates a new note.
Creates a new note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertNewNote3( _
   ByVal UpperText As System.String, _
   ByVal NoLeader As System.Boolean, _
   ByVal BentLeader As System.Boolean, _
   ByVal ArrowStyle As System.Short, _
   ByVal LeaderSide As System.Short, _
   ByVal Angle As System.Double, _
   ByVal BalloonStyle As System.Short, _
   ByVal BalloonFit As System.Short, _
   ByVal SmartArrow As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim UpperText As System.String
Dim NoLeader As System.Boolean
Dim BentLeader As System.Boolean
Dim ArrowStyle As System.Short
Dim LeaderSide As System.Short
Dim Angle As System.Double
Dim BalloonStyle As System.Short
Dim BalloonFit As System.Short
Dim SmartArrow As System.Boolean
 
instance.InsertNewNote3(UpperText, NoLeader, BentLeader, ArrowStyle, LeaderSide, Angle, BalloonStyle, BalloonFit, SmartArrow)
```

```

void InsertNewNote3( 
   System.string UpperText,
   System.bool NoLeader,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide,
   System.double Angle,
   System.short BalloonStyle,
   System.short BalloonFit,
   System.bool SmartArrow
)
```

```

void InsertNewNote3( 
   System.String^ UpperText,
   System.bool NoLeader,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide,
   System.double Angle,
   System.short BalloonStyle,
   System.short BalloonFit,
   System.bool SmartArrow
) 
```

#### Parameters

*UpperText*
:   Upper-text string to be put in the note

*NoLeader*
:   True for no leaderline, false if not

*BentLeader*
:   True for a bent leaderline, false if not

*ArrowStyle*
:   Arrowhead type as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

*LeaderSide*
:   Leaderline side as defined in [swLeaderSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderSide_e.html)

*Angle*
:   Text angle

*BalloonStyle*
:   Balloon style type as defined in [swBalloonStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html)

*BalloonFit*
:   Balloon fit type as defined in [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html)

*SmartArrow*
:   If true then the arrow style specified in Options > Detailing is used for the arrows, if false then the ArrowStyle argument is used

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IInsertNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertNote.md)  
[IModelDoc2::InsertNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNote.md)  
[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[IDrawingDoc::InsertNewNote2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.md)
