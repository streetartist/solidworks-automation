# InsertNewNote Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote`

Obsolete. Superseded by IDrawingDoc::InsertNewNote2.
Obsolete. Superseded by [IDrawingDoc::InsertNewNote2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertNewNote( _
   ByVal Text As System.String, _
   ByVal NoLeader As System.Boolean, _
   ByVal BalloonNote As System.Boolean, _
   ByVal BentLeader As System.Boolean, _
   ByVal ArrowStyle As System.Short, _
   ByVal LeaderSide As System.Short _
) 
```

```

Dim instance As IDrawingDoc
Dim Text As System.String
Dim NoLeader As System.Boolean
Dim BalloonNote As System.Boolean
Dim BentLeader As System.Boolean
Dim ArrowStyle As System.Short
Dim LeaderSide As System.Short
 
instance.InsertNewNote(Text, NoLeader, BalloonNote, BentLeader, ArrowStyle, LeaderSide)
```

```

void InsertNewNote( 
   System.string Text,
   System.bool NoLeader,
   System.bool BalloonNote,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide
)
```

```

void InsertNewNote( 
   System.String^ Text,
   System.bool NoLeader,
   System.bool BalloonNote,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide
) 
```

#### Parameters

*Text*

*NoLeader*

*BalloonNote*

*BentLeader*

*ArrowStyle*

*LeaderSide*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
