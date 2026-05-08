# AddOrdinateDimension Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddOrdinateDimension`

Obsolete. Superseded by IModelDocExtension::AddOrdinateDimension.
Obsolete. Superseded by [IModelDocExtension::AddOrdinateDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddOrdinateDimension( _
   ByVal DimType As System.Integer, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim DimType As System.Integer
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim value As System.Boolean
 
value = instance.AddOrdinateDimension(DimType, LocX, LocY, LocZ)
```

```

System.bool AddOrdinateDimension( 
   System.int DimType,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

```

System.bool AddOrdinateDimension( 
   System.int DimType,
   System.double LocX,
   System.double LocY,
   System.double LocZ
) 
```

#### Parameters

*DimType*

*LocX*

*LocY*

*LocZ*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
