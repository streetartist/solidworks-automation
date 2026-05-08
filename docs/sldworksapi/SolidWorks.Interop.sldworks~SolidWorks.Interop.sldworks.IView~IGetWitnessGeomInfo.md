# IGetWitnessGeomInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWitnessGeomInfo`

Gets the geometry data for all of the virtual sharp witness lines in this drawing view.
Gets the geometry data for all of the virtual sharp witness lines in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetWitnessGeomInfo( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

```

Dim instance As IView
Dim ArraySize As System.Integer
Dim value As System.Double
 
value = instance.IGetWitnessGeomInfo(ArraySize)
```

```

System.double IGetWitnessGeomInfo( 
   System.int ArraySize
)
```

```

System.double IGetWitnessGeomInfo( 
   System.int ArraySize
) 
```

#### Parameters

*ArraySize*
:   Size of the virtual sharp witness line geometry data array (see **Remarks**)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

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
> 0 (**NOTE:** 0 = witness line data),
>
> number (m) of witness lines,
>
> witness line 1[start\_point[x,y,z], end\_point[x,y,z&cd;
>
> ...
>
> witness line m[start\_point[x,y,z], end\_point[x,y,z&cd;,
>
> 1 (**NOTE:** 1 = witness arc data),
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

Before calling this method, call [IView::GetWitnessEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWitnessEntitiesCount.md) to get the size of the array returned by this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetWitnessGeomInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWitnessGeomInfo.md)
