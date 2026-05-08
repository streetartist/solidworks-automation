# IView3D Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D`

Allows access to a 3D View of a part or assembly.
Allows access to a 3D View of a part or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IView3D 
```

```

Dim instance As IView3D
```

```

public interface IView3D 
```

```

public interface class IView3D 
```

Remarks

This interface supports SOLIDWORKS Model Based Definition (MBD), which is an integrated drawingless manufacturing solution for SOLIDWORKS. Use [ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.md) to load the MBD add-in.

See the SOLIDWORKS Help for details about MBD.

Example

[Capture 3D View (VBA)](Capture_3DView_Example_VB.htm)  
[Capture 3D View (VB.NET)](Capture_3DView_Example_VBNET.htm)  
[Capture 3D View (C#)](Capture_3DView_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::Get3DViewCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewCount.md)  
[IModelDocExtension::Get3DViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DViewNames.md)  
[IModelDocExtension::Refresh3DViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Refresh3DViews.md)  
[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md)
