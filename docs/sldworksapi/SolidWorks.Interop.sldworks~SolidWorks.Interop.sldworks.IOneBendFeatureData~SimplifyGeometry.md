# SimplifyGeometry Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~SimplifyGeometry`

Gets or sets whether to simplify the geometry for this bend feature.
Gets or sets whether to simplify the geometry for this bend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SimplifyGeometry As System.Boolean
```

```

Dim instance As IOneBendFeatureData
Dim value As System.Boolean
 
instance.SimplifyGeometry = value
 
value = instance.SimplifyGeometry
```

```

System.bool SimplifyGeometry {get; set;}
```

```

property System.bool SimplifyGeometry {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to simplify the geometry, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.md)  
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.md)
