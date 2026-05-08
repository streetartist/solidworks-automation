# ISplineHandle Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle`

Provides access to spline handles.
Provides access to spline handles.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISplineHandle 
```

```

Dim instance As ISplineHandle
```

```

public interface ISplineHandle 
```

```

public interface class ISplineHandle 
```

Remarks

To enable spline tangency and curvature handles, set [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) swDisplayAllSplineHandles to True.

NOTE: [ISelectionMgr::GetSelectedObjectType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md) returns swSelMANIPULATORS for a spline handle.

Example

[Get and Set Spline Handles (VBA)](Get_and_Set_Spline_Handles_Example_VB.htm)  
[Get and Set Spline Handles (VB.NET)](Get_and_Set_Spline_Handles_Example_VBNET.htm)  
[Get and Set Spline Handles (C#)](Get_and_Set_Spline_Handles_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)
