# UseNormalPlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~UseNormalPlane`

Gets or sets whether to:
Gets or sets whether to:

- Use the plane normal to the selected plane
- Automatically size the plane to either the geometry on which it is created or to the bounding box of the model geometry

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseNormalPlane As System.Boolean
```

```

Dim instance As IRefPlaneFeatureData
Dim value As System.Boolean
 
instance.UseNormalPlane = value
 
value = instance.UseNormalPlane
```

```

System.bool UseNormalPlane {get; set;}
```

```

property System.bool UseNormalPlane {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use a plane normal to the selected plane and automatically size the plane, false to not

Remarks

If this property is true, then you can get or set [IRefPlaneFeatureData::Angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Angle.md).

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) topic for details about reference planes and this interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)  
[IRefPlaneFeatureData::AutoSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~AutoSize.md)
