# IGetCurveParams Method (ICoEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams`

Gets the curve parameters.
Gets the curve parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCurveParams() As System.Double
```

```

Dim instance As ICoEdge
Dim value As System.Double
 
value = instance.IGetCurveParams()
```

```

System.double IGetCurveParams()
```

```

System.double IGetCurveParams(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value format is an array of 10 doubles:

- retval[0]  X startpoint
- retval[1]  Y startpoint
- retval[2]  Z startpoint
- retval[3]  X endpoint
- retval[4]  Y endpoint
- retval[5]  Z endpoint
- retval[6]  startParam
- retval[7]  endParam
- retval[8]  sense (Not used)
- retval[9]  curve type (Not used)

Example

[Get Edge Data By Name (C++)](Get_Edge_Data_By_Name_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)  
[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.md)  
[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)  
[IEdge::GetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2.md)  
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams.md)
