# IGetTrimCurveTopology Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopology`

Gets the trim curve topology for this face.
Gets the trim curve topology for this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTrimCurveTopology() As System.Object
```

```

Dim instance As IFace2
Dim value As System.Object
 
value = instance.IGetTrimCurveTopology()
```

```

System.object IGetTrimCurveTopology()
```

```

System.Object^ IGetTrimCurveTopology(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of coedges, vertices, and NULLs (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method returns a list of coedges, vertices, and NULLs. You must call [IFace2::GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md) or [IFace2::IGetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2.md) before calling this method.

This method returns a list of proper edges corresponding to the list of SP curves from IFace2::GetTrimCurves2 or IFace2::IGetTrimCurves2. Otherwise, this method prompts the user for the list of edges that the software thinks are on the face. These two lists differ in order and content.

Use [IFace2::GetTrimCurveTopologyTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopology.md) or [IFace2::IGetTrimCurveTopologyTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopology.md) to get an array of types corresponding to the returned objects.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IGetTrimCurveSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2.md)  
[IFace2::GetTrimCurveTopologyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyCount.md)
