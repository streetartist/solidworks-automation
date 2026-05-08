# IFindMinimumRadius Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IFindMinimumRadius`

Finds the minimum radius of curvature of the selected curve and its position and u-v parameters.
Finds the minimum radius of curvature of the selected curve and its position and u-v parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFindMinimumRadius( _
   ByRef Bound As System.Double, _
   ByRef NumOfRadius As System.Integer, _
   ByRef Radius As System.Object, _
   ByRef Location As System.Object, _
   ByRef Parameter As System.Object _
) As System.Boolean
```

```

Dim instance As ICurve
Dim Bound As System.Double
Dim NumOfRadius As System.Integer
Dim Radius As System.Object
Dim Location As System.Object
Dim Parameter As System.Object
Dim value As System.Boolean
 
value = instance.IFindMinimumRadius(Bound, NumOfRadius, Radius, Location, Parameter)
```

```

System.bool IFindMinimumRadius( 
   ref System.double Bound,
   out System.int NumOfRadius,
   out System.object Radius,
   out System.object Location,
   out System.object Parameter
)
```

```

System.bool IFindMinimumRadius( 
   System.double% Bound,
   [Out] System.int NumOfRadius,
   [Out] System.Object^ Radius,
   [Out] System.Object^ Location,
   [Out] System.Object^ Parameter
) 
```

#### Parameters

*Bound*
:   Array containing the start and end boundary parameters (see **Remarks**)

*NumOfRadius*
:   Number of radius returned; can be 0 or 1

*Radius*
:   Minimum radius of curvature (see **Remarks**)

*Location*
:   [Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) where minimum radius curvature occurred  (see **Remarks**)

*Parameter*
:   Curve parameter  (see **Remarks**)

#### Return Value

True if operation succeeds, false if it fails

Remarks

The search is confined to the portion of the selected curve lying inside of Bound.

COM returns these data types for these parameters:

- Radius: VARIANT of SafeDoubleArray
- Location: VARIANT of SafeDispatchArray of [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)
- Parameter: VARIANT of SafeDoubleArray

Example

**Unmanaged C++ COM:**

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
>  
>
> CComPtr<ISelectionMgr> swSelMgr;
>
> iModelDoc2->get\_**ISelectionManager**(&swSelMgr);
>
> struct IDispatch\* pDispSelection;
>
> CComPtr<IEdge> swEdge;
>
> swSelMgr->**GetSelectedObject6**(1,-1,&pDispSelection);
>
> pDispSelection->QueryInterface(\_\_uuidof(IEdge),reinterpret\_cast<void\*\*>(&swEdge));
>
> pDispSelection->Release();
>
>  
>
> double boundArr[2];
>
> CComPtr<ICurve> swCurve;
>
> swEdge->**IGetCurve**(&swCurve);
>
>  
>
> VARIANT\_BOOL isClose,isPeriodic,testRetVal;
>
> swCurve->**GetEndParams**(&boundArr[0],&boundArr[1],&isClose,&isPeriodic,&testRetVal);
>
>  
>
> long numOfRadius(0);
>
> VARIANT radius,Location,UVParameter;
>
> VARIANT\_BOOL status(FALSE);
>
> swCurve->**IFindMinimumRadius**(boundArr,&numOfRadius,&radius,&Location,&UVParameter,&status);
>
>  
>
> SafeDoubleArray radiusSA(radius);
>
> double test1 = radiusSA[0];
>
>  
>
> SafeDISPATCHArray locationSA(Location);
>
>  
>
> CComPtr<IMathPoint> swMathPoint1;
>
> locationSA[0]->QueryInterface(\_\_uuidof(IMathPoint),reinterpret\_cast<void\*\*>(&swMathPoint1));
>
>  
>
> double locationArra1[3];
>
>  
>
> swMathPoint1->get\_**IArrayData**(locationArra1);
>
>  
>
> SafeDoubleArray UVParameterSA(UVParameter);
>
>  
>
> double uvpara1 = UVParameterSA[0];
>
> return S\_OK;

}

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)  
[ICurve::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~FindMinimumRadius.md)  
[ISurface::FindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~FindMinimumRadius.md)  
[ISurface::IFindMinimumRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IFindMinimumRadius.md)  
[ICurve::GetEndParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEndParams.md)
