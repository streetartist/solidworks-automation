# InsertNewNote3 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertNewNote3`

Obsolete. Superseded by IModelDoc2::InsertNewNote3.
Obsolete. Superseded by [IModelDoc2::InsertNewNote3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNewNote3.md).

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

Dim instance As IModelDoc
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

*NoLeader*

*BentLeader*

*ArrowStyle*

*LeaderSide*

*Angle*

*BalloonStyle*

*BalloonFit*

*SmartArrow*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
