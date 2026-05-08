# UpdatePlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~UpdatePlane`

Gets or sets whether to update this reference plane so that it is parallel to the screen.
Gets or sets whether to update this reference plane so that it is parallel to the screen.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UpdatePlane As System.Boolean
```

```

Dim instance As IRefPlaneFeatureData
Dim value As System.Boolean
 
instance.UpdatePlane = value
 
value = instance.UpdatePlane
```

```

System.bool UpdatePlane {get; set;}
```

```

property System.bool UpdatePlane {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to update the reference plane so that it is parallel to the screen, false to not

Example

[Update Plane (C#)](Update_Plane_Example_CSharp.htm)  
[Update Plane (VB.NET)](Update_Plane_Example_VBNET.htm)  
[Update Plane (VBA)](Update_Plane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)
