# GetRefAxisParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~GetRefAxisParams`

Gets information for a reference axis.
Gets information for a reference axis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRefAxisParams() As System.Object
```

```

Dim instance As IRefAxis
Dim value As System.Object
 
value = instance.GetRefAxisParams()
```

```

System.object GetRefAxisParams()
```

```

System.Object^ GetRefAxisParams(); 
```

#### Return Value

Array of doubles (see [Remarks](#Remarks))

Remarks

The return value is the following array of doubles:

[ StartPt[3], EndPt[3] ]

where:

- StartPt[3] = array of three values describing the x,y,z start point of the reference axis.
- EndPt[3] = array of three values describing the x,y,z end point of the reference axis.

Example

[Get Parameters for Reference Axis (VBA)](Get_Parameters_for_Reference_Axis_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefAxis Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)  
[IRefAxis Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis_members.md)  
[IRefAxis::IGetRefAxisParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~IGetRefAxisParams.md)
