# ISurfaceParameterizationData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData`

Allows access to the parameterization data of a surface.
Allows access to the parameterization data of a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISurfaceParameterizationData 
```

```

Dim instance As ISurfaceParameterizationData
```

```

public interface ISurfaceParameterizationData 
```

```

public interface class ISurfaceParameterizationData 
```

Remarks

If a surface is periodic in one direction (cylinder, cone, torus, sphere), then U is the periodic direction.

The -10000 to 10000 parameter range is the modeling limit for the modeler. This means that the values are effectively infinite in size. To get the parameter range from a given face, use [IFace2::GetBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetBox.md) or [IFace2::IGetBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetBox.md), [ISurface::GetClosestPointOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetClosestPointOn.md) or [ISurface::IGetClosestPointOn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetClosestPointOn.md), and [ISurface::ReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ReverseEvaluate.md) or [ISurface::IReverseEvaluate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IReverseEvaluate.md).  These methods provide a true parameter range that the face is using on the surface.

Example

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)  
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)  
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceParameterizationData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.md)  
[ISurface::GetBSurfParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams3.md)
