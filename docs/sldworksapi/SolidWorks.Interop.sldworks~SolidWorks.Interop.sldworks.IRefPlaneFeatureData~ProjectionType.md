# ProjectionType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ProjectionType`

Gets or sets the projection type for this on-surface reference plane feature.
Gets or sets the projection type for this on-surface reference plane feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProjectionType As System.Integer
```

```

Dim instance As IRefPlaneFeatureData
Dim value As System.Integer
 
instance.ProjectionType = value
 
value = instance.ProjectionType
```

```

System.int ProjectionType {get; set;}
```

```

property System.int ProjectionType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of a plane on a surface as defined in [swOnSurfacePlaneProjectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOnSurfacePlaneProjectType_e.html)

Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) topic for details about reference planes and this interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)
