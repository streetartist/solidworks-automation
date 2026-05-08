# FieldOfViewDepth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewDepth`

Gets the camera's depth of the field of view.
Gets the camera's depth of the field of view.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FieldOfViewDepth As System.Double
```

```

Dim instance As ICamera
Dim value As System.Double
 
instance.FieldOfViewDepth = value
 
value = instance.FieldOfViewDepth
```

```

System.double FieldOfViewDepth {get; set;}
```

```

property System.double FieldOfViewDepth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Camera's depth of the field of view

Remarks

This property is only meaningful for a perspective camera.

Example

[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)  
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)  
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::FieldOfViewAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewAngle.md)  
[ICamera::FieldOfViewHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewHeight.md)  
[ICamera::Perspective Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Perspective.md)
