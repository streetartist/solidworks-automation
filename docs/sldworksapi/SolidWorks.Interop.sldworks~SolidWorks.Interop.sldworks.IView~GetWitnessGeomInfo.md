# GetWitnessGeomInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWitnessGeomInfo`

Gets the geometry data for all of the virtual sharp witness lines in this drawing view.
Gets the geometry data for all of the virtual sharp witness lines in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWitnessGeomInfo() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetWitnessGeomInfo()
```

```

System.object GetWitnessGeomInfo()
```

```

System.Object^ GetWitnessGeomInfo(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

This method returns an array containing the following data for each virtual sharp in the view:

> [*color\_value*,
>
> [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) option (-1 if no line style is specified),
>
> [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) option (-1 if no line weight is specified),
>
> layer ID (-1 if no layer is specified),
>
> [swLayerOverride\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLayerOverride_e.html) option,
>
> 0 (**NOTE:**  0 = witness line data),
>
> number (m) of witness lines,
>
> witness line 1[start\_point[x,y,z], end\_point[x,y,z&cd;
>
> ...
>
> witness line m[start\_point[x,y,z], end\_point[x,y,z&cd;,
>
> 1 (**NOTE**: 1 = witness arc data),
>
> number (n) of witness arcs,
>
> witness arc 1[start\_point[x,y,z], end\_point[x,y,z], center\_point[x,y,z], normal\_point[x,y,z&cd;
>
> ...
>
> witness arc n[start\_point[x,y,z], end\_point[x,y,z], center\_point[x,y,z], normal\_point[x,y,z&cd;]

Where:

> *color\_value =* MAX(MIN(*red\_rgb\_value*,255),0) *+* MAX(MIN(*green\_rgb\_value*,255),0)\*16\*16 *+* MAX(MIN(*blue\_rgb\_value*,255),0)\*16\*16\*16\*16

Call [IView::GetWitnessEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWitnessEntitiesCount.md) to get the size of the array returned by this method.

Example

[Get Virtual Sharp Witness Line Data (C#)](Get_Virtual_Sharp_Witness_Line_Data_Example_CSharp.htm)  
[Get Virtual Sharp Witness Line Data (VB.NET)](Get_Virtual_Sharp_Witness_Line_Data_Example_VBNET.htm)  
[Get Virtual Sharp Witness Line Data (VBA)](Get_Virtual_Sharp_Witness_Line_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetWitnessGeomInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWitnessGeomInfo.md)
