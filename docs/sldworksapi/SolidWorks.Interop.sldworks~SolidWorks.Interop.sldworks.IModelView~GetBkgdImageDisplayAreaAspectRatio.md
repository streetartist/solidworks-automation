# GetBkgdImageDisplayAreaAspectRatio Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetBkgdImageDisplayAreaAspectRatio`

Gets the aspect ratio (width/height) of the area of the window where the background image is displayed.
Gets the aspect ratio (width/height) of the area of the window where the background image is displayed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBkgdImageDisplayAreaAspectRatio() As System.Double
```

```

Dim instance As IModelView
Dim value As System.Double
 
value = instance.GetBkgdImageDisplayAreaAspectRatio()
```

```

System.double GetBkgdImageDisplayAreaAspectRatio()
```

```

System.double GetBkgdImageDisplayAreaAspectRatio(); 
```

#### Return Value

Aspect ratio (width/height) of the area of the window where the background image is displayed, or -1 if there is no background image or if the image covers the entire window

Remarks

For use with ray-trace rendering engines to match SOLIDWORKS' display.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
