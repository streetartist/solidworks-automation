# ICreateSheetFromSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface`

Obsolete. Superseded by IModeler::ICreateSheetFromSurface2.
Obsolete. Superseded by [IModeler::ICreateSheetFromSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSheetFromSurface( _
   ByVal SurfaceIn As Surface, _
   ByRef UvRange As System.Double _
) As Body
```

```

Dim instance As IModeler
Dim SurfaceIn As Surface
Dim UvRange As System.Double
Dim value As Body
 
value = instance.ICreateSheetFromSurface(SurfaceIn, UvRange)
```

```

Body ICreateSheetFromSurface( 
   Surface SurfaceIn,
   ref System.double UvRange
)
```

```

Body^ ICreateSheetFromSurface( 
   Surface^ SurfaceIn,
   System.double% UvRange
) 
```

#### Parameters

*SurfaceIn*

*UvRange*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
