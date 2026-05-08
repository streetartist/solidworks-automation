# IFindMinimumRadius Method (ISurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IFindMinimumRadius`

Gets the minimum radius of curvature for the selected surface.
Gets the minimum radius of curvature for the selected surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFindMinimumRadius( _
   ByRef UBound As System.Double, _
   ByRef VBound As System.Double, _
   ByRef NumOfRadius As System.Integer, _
   ByRef Radius As System.Object, _
   ByRef Location As System.Object, _
   ByRef UVParameter As System.Object _
) As System.Boolean
```

```

Dim instance As ISurface
Dim UBound As System.Double
Dim VBound As System.Double
Dim NumOfRadius As System.Integer
Dim Radius As System.Object
Dim Location As System.Object
Dim UVParameter As System.Object
Dim value As System.Boolean
 
value = instance.IFindMinimumRadius(UBound, VBound, NumOfRadius, Radius, Location, UVParameter)
```

```

System.bool IFindMinimumRadius( 
   ref System.double UBound,
   ref System.double VBound,
   out System.int NumOfRadius,
   out System.object Radius,
   out System.object Location,
   out System.object UVParameter
)
```

```

System.bool IFindMinimumRadius( 
   System.double% UBound,
   System.double% VBound,
   [Out] System.int NumOfRadius,
   [Out] System.Object^ Radius,
   [Out] System.Object^ Location,
   [Out] System.Object^ UVParameter
) 
```

#### Parameters

*UBound*
:   MinMax UParameter

*VBound*
:   MinMax VParameter

*NumOfRadius*
:   Number of radius; can be 0, 1, or 2

*Radius*
:   Minimum radius of curvature (see **Remarks**)

*Location*
:   [Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) where the minimum radius curvature occurred (see **Remarks**)

*UVParameter*
:   [UV parameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md); because points are UV, third ordinates are 0 (see **Remarks**)

#### Return Value

True if operation succeeds, false if it fails

Remarks

The search is confined to the portion of the selected curve lying inside of UBound and VBound.

COM returns these data types for these parameters:

- Radius: VARIANT of SafeDoubleArray
- Location: VARIANT of SafeDispatchArray of [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)
- UVParameter: VARIANT of SafeDispatchArray of [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

Example

**In-process, unmanaged C++:**

/////////////////////////////////////////////////////////////////////////////

// IMinRadius implementation

STDMETHODIMP CMinRadius::StartNotepad()

{

> // TODO: Add your implementation code here
>
> CComPtr<IModelDoc> iModelDoc2;
>
> m\_iSldWorks->get\_**IActiveDoc**(&iModelDoc2);
>
> CComPtr<ISelectionMgr> swSelMgr;
>
> iModelDoc2->get\_**ISelectionManager**(&swSelMgr);
>
> struct IDispatch\* pDispSelection;
>
> CComPtr<IFace2> swFace;
>
> swSelMgr->**GetSelectedObject6**(1,-1,&pDispSelection);
>
> pDispSelection->QueryInterface(\_\_uuidof(IFace2),reinterpret\_cast<void\*\*>(&swFace));
>
> pDispSelection->Release();
>
> double boundArr[4];
>
> swFace->**IGetUVBounds** ( boundArr );
>
> double UBound[2] = {boundArr[0],boundArr[1]};
>
> double VBound[2] = {boundArr[2],boundArr[3]};
>
> CComPtr<ISurface> swSurface;
>
> swFace->**IGetSurface**(&swSurface);
>
> long numOfRadius(0);
>
> VARIANT radius,Location,UVParameter;
>
> VARIANT\_BOOL status(FALSE);
>
> swSurface->**IFindMinimumRadius**(UBound,VBound,&numOfRadius,&radius,&Location,&UVParameter,&status);
>
> SafeDoubleArray radiusSA(radius);
>
> double test1 = radiusSA[0];
>
> double test2 = radiusSA[1];
>
> SafeDISPATCHArray locationSA(Location);
>
> CComPtr<IMathPoint> swMathPoint1;
>
> CComPtr<IMathPoint> swMathPoint2;
>
> locationSA[0]->QueryInterface(\_\_uuidof(IMathPoint),reinterpret\_cast<void\*\*>(&swMathPoint1));
>
> locationSA[1]->QueryInterface(\_\_uuidof(IMathPoint),reinterpret\_cast<void\*\*>(&swMathPoint2));
>
> double locationArra1[3];
>
> double locationArra2[3];
>
> swMathPoint1->get\_**IArrayData**(locationArra1);
>
> swMathPoint2->get\_**IArrayData**(locationArra2);
>
> SafeDISPATCHArray UVParameterSA(UVParameter);
>
> return S\_OK;

}

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~FindMinimumRadius.md)  
[IFace2::IGetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetUVBounds.md)  
[IFace2::GetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetUVBounds.md)  
[ICurve::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~FindMinimumRadius.md)  
[ICurve::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IFindMinimumRadius.md)  
[ISurface::IParameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.md)  
[ISurface::Parameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.md)
