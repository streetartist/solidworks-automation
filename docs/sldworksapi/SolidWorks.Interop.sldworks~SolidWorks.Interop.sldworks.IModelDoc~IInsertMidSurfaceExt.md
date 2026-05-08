# IInsertMidSurfaceExt Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IInsertMidSurfaceExt`

Obsolete. Superseded by IModelDoc2::IInsertMidSurfaceExt.
Obsolete. Superseded by [IModelDoc2::IInsertMidSurfaceExt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertMidSurfaceExt.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertMidSurfaceExt( _
   ByVal Placement As System.Double, _
   ByVal KnitFlag As System.Boolean _
) As MidSurface
```

```

Dim instance As IModelDoc
Dim Placement As System.Double
Dim KnitFlag As System.Boolean
Dim value As MidSurface
 
value = instance.IInsertMidSurfaceExt(Placement, KnitFlag)
```

```

MidSurface IInsertMidSurfaceExt( 
   System.double Placement,
   System.bool KnitFlag
)
```

```

MidSurface^ IInsertMidSurfaceExt( 
   System.double Placement,
   System.bool KnitFlag
) 
```

#### Parameters

*Placement*

*KnitFlag*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
