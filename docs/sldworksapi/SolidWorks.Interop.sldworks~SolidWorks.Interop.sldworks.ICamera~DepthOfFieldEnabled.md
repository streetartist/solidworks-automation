# DepthOfFieldEnabled Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~DepthOfFieldEnabled`

Gets whether depth of field effects are enabled or disabled.
Gets whether depth of field effects are enabled or disabled.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DepthOfFieldEnabled As System.Boolean
```

```

Dim instance As ICamera
Dim value As System.Boolean
 
instance.DepthOfFieldEnabled = value
 
value = instance.DepthOfFieldEnabled
```

```

System.bool DepthOfFieldEnabled {get; set;}
```

```

property System.bool DepthOfFieldEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if depth of field effects are enabled, false if they are disabled

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
[ICamera::DepthOfFieldOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~DepthOfFieldOffset.md)
