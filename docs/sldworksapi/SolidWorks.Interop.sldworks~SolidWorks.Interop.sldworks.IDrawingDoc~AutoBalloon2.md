# AutoBalloon2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon2`

Obsolete. Superseded by IDrawingDoc::AutoBalloon3.
Obsolete. Superseded by [IDrawingDoc::AutoBalloon3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AutoBalloon2( _
   ByVal Layout As System.Integer, _
   ByVal IgnoreMultiple As System.Boolean _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim Layout As System.Integer
Dim IgnoreMultiple As System.Boolean
Dim value As System.Object
 
value = instance.AutoBalloon2(Layout, IgnoreMultiple)
```

```

System.object AutoBalloon2( 
   System.int Layout,
   System.bool IgnoreMultiple
)
```

```

System.Object^ AutoBalloon2( 
   System.int Layout,
   System.bool IgnoreMultiple
) 
```

#### Parameters

*Layout*

*IgnoreMultiple*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
