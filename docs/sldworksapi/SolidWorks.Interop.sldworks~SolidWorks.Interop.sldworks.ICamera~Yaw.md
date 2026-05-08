# Yaw Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Yaw`

Gets or sets the yaw (side-to-side angle) of a floating camera.
Gets or sets the yaw (side-to-side angle) of a [floating camera](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Type.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Yaw As System.Double
```

```

Dim instance As ICamera
Dim value As System.Double
 
instance.Yaw = value
 
value = instance.Yaw
```

```

System.double Yaw {get; set;}
```

```

property System.double Yaw {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Yaw

Example

[Insert and Rotate Camera (C#)](Insert_and_Rotate_Camera_Example_CSharp.htm)  
[Insert and Rotate Camera (VB.NET)](Insert_and_Rotate_Camera_Example_VBNET.htm)  
[Insert and Rotate Camera (VBA)](Insert_and_Rotate_Camera_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)
