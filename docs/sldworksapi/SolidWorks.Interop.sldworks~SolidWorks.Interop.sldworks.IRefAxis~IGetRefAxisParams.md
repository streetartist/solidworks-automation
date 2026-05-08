# IGetRefAxisParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~IGetRefAxisParams`

Gets information for a reference axis.
Gets information for a reference axis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetRefAxisParams() As System.Double
```

```

Dim instance As IRefAxis
Dim value As System.Double
 
value = instance.IGetRefAxisParams()
```

```

System.double IGetRefAxisParams()
```

```

System.double IGetRefAxisParams(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see [Remarks](#Remarks))

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is the following array of doubles:

[ StartPt[3], EndPt[3] ]

where:

- StartPt[3] = array of three values describing the x,y,z start point of the reference axis.
- EndPt[3] = array of three values describing the x,y,z end point of the reference axis.

Example

[Get Info on Plane-Axis (C++)](Get_Info_on_Plane_Axis_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefAxis Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)  
[IRefAxis Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis_members.md)  
[IRefAxis::GetRefAxisParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~GetRefAxisParams.md)
