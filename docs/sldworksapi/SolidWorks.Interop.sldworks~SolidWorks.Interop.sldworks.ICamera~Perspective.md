# Perspective Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Perspective`

Gets whether the camera is in perspective mode or not.
Gets whether the camera is in perspective mode or not.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Perspective As System.Boolean
```

```

Dim instance As ICamera
Dim value As System.Boolean
 
instance.Perspective = value
 
value = instance.Perspective
```

```

System.bool Perspective {get; set;}
```

```

property System.bool Perspective {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if camera is in perspective mode, false if not

Example

[Insert Camera (C#)](Insert_Cavity_Example_CSharp.htm)  
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)  
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)  
[ICamera::FieldOfViewAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewAngle.md)  
[ICamera::FieldOfViewDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewDepth.md)  
[ICamera::FieldOfViewHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewHeight.md)
