# CreateDrawViewFromModelView2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView2`

Obsolete. Superseded by IDrawingDoc::CreateDrawViewFromModelView3.
Obsolete. Superseded by [IDrawingDoc::CreateDrawViewFromModelView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateDrawViewFromModelView2( _
   ByVal ModelName As System.String, _
   ByVal ViewName As System.String, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double _
) As View
```

```

Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ViewName As System.String
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim value As View
 
value = instance.CreateDrawViewFromModelView2(ModelName, ViewName, LocX, LocY, LocZ)
```

```

View CreateDrawViewFromModelView2( 
   System.string ModelName,
   System.string ViewName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

```

View^ CreateDrawViewFromModelView2( 
   System.String^ ModelName,
   System.String^ ViewName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
) 
```

#### Parameters

*ModelName*

*ViewName*

*LocX*

*LocY*

*LocZ*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
