# AutoDimension Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~AutoDimension`

Obsolete. Superseded by ISketch::AutoDimension2.
Obsolete. Superseded by [ISketch::AutoDimension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~AutoDimension2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AutoDimension( _
   ByVal EntitiesToDimension As System.Integer, _
   ByVal HorizontalScheme As System.Integer, _
   ByVal HorizontalPlacement As System.Integer, _
   ByVal VerticalScheme As System.Integer, _
   ByVal VerticalPlacement As System.Integer _
) As System.Integer
```

```

Dim instance As ISketch
Dim EntitiesToDimension As System.Integer
Dim HorizontalScheme As System.Integer
Dim HorizontalPlacement As System.Integer
Dim VerticalScheme As System.Integer
Dim VerticalPlacement As System.Integer
Dim value As System.Integer
 
value = instance.AutoDimension(EntitiesToDimension, HorizontalScheme, HorizontalPlacement, VerticalScheme, VerticalPlacement)
```

```

System.int AutoDimension( 
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
)
```

```

System.int AutoDimension( 
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
) 
```

#### Parameters

*EntitiesToDimension*

*HorizontalScheme*

*HorizontalPlacement*

*VerticalScheme*

*VerticalPlacement*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)
