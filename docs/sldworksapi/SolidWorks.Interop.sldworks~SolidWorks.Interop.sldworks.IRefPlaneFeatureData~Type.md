# Type Property (IRefPlaneFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type`

Gets the type of reference plane created in SOLIDWORKS 2009 or earlier. Can also get whether a constraint-based reference plane created in SOLIDWORKS 2010 or has angle or offset distance references. NOTE: This property is a get-only property. Set i
Gets the type of reference plane created in SOLIDWORKS 2009 or earlier. Can also get whether a constraint-based reference plane created in SOLIDWORKS 2010 or has angle or offset distance references.  
  
 **NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Type As System.Integer
```

```

Dim instance As IRefPlaneFeatureData
Dim value As System.Integer
 
instance.Type = value
 
value = instance.Type
```

```

System.int Type {get; set;}
```

```

property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of reference plane as defined in [swRefPlaneType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneType_e.html)

Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) topic for details about reference planes and this interface.

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
