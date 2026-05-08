# AspectRatio Property (ICamera)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~AspectRatio`

Gets the aspect ratio (width/height) of the field of view rectangle for the camera.
Gets the aspect ratio (width/height) of the field of view rectangle for the camera.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AspectRatio As System.Double
```

```

Dim instance As ICamera
Dim value As System.Double
 
instance.AspectRatio = value
 
value = instance.AspectRatio
```

```

System.double AspectRatio {get; set;}
```

```

property System.double AspectRatio {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Width/height ratio of the view rectangle for the camera

Remarks

The rectangle is best-fit into a rendering window to determine the actual composition.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.md)  
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.md)
