# Type2 Property (IRefPlaneFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type2`

Gets whether the reference plane is constraint based; thus, created in SOLIDWORKS 2010 and later.
Gets whether the reference plane is constraint based; thus, created in SOLIDWORKS 2010 and later.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Type2 As System.Integer
```

```

Dim instance As IRefPlaneFeatureData
Dim value As System.Integer
 
instance.Type2 = value
 
value = instance.Type2
```

```

System.int Type2 {get; set;}
```

```

property System.int Type2 {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of reference plane as defined in [swRefPlaneType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneType_e.html) (see **Remarks**)

Remarks

If IRefPlaneFeatureData::Type2 returns swRefPlaneConstraintBase, then the reference plane is constraint based and was created in SOLIDWORKS 2010 or later. To determine if a constraint-based reference plane has angle or offset distances references, call [IRefPlaneFeatureData::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type.md):

- swRefPlaneAngle is returned for angle references.
- swRefPlaneDistance is returned for offset distance references.

Otherwise, the reference plane is not constraint based and was created in SOLIDWORKS 2009 or earlier. Call [IRefPlaneFeatureData::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type.md) to determine its type.

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) topic for details about reference planes and this interface.

Example

[Insert Reference Plane (C#)](Insert_Reference_Plane_Example_CSharp.htm)  
[Insert Reference Plane (VB.NET)](Insert_Reference_Plane_Example_VBNET.htm)  
[Insert Reference Plane (VBA)](Insert_Reference_Plane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)  
[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)
