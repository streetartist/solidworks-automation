# ICreateBoundedSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBoundedSurface`

Creates a bounded surface from an independent base surface.
Creates a bounded surface from an independent base surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreateBoundedSurface( _
   ByVal UOpt As System.Boolean, _
   ByVal VOpt As System.Boolean, _
   ByRef UvParams As System.Double _
) 
```

```

Dim instance As IBody2
Dim UOpt As System.Boolean
Dim VOpt As System.Boolean
Dim UvParams As System.Double
 
instance.ICreateBoundedSurface(UOpt, VOpt, UvParams)
```

```

void ICreateBoundedSurface( 
   System.bool UOpt,
   System.bool VOpt,
   ref System.double UvParams
)
```

```

void ICreateBoundedSurface( 
   System.bool UOpt,
   System.bool VOpt,
   System.double% UvParams
) 
```

#### Parameters

*UOpt*
:   True if U parameter range is given in uvData, false for the entire U parameter range

*VOpt*
:   True if V parameter range is given in uvData, false for the entire V parameter range

*UvParams*
:   Array of 4 doubles (see **Remarks**)

Remarks

Before you use this method, you must call one of the base surface creation methods, such as [IBody2::ICreateBsplineSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBsplineSurface.md).

The UOpt and VOpt arguments allow the application to supply parameter range information so that a bounded surface can be made up from part of the base surface. If UOpt and VOpt are both set to false, then SOLIDWORKS uses the entire parameter ranges. This method fails for surfaces with infinite parameter ranges.

UvParams contains 4 doubles describing the UV parameter ranges.

|  |  |
| --- | --- |
| U parameter range | uvData[0] and uvData[1]; UvData[0] must be less than uvData[1] |
| V parameter range | uvData[2] and uvData[3]; UvData[2] must be less than uvData[3] |

To construct a solid body from bounded surfaces, call [IPartDoc::ICreateNewBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateNewBody2.md) first, which arranges for a placeholder for this bounded surface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreateBoundedSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBoundedSurface.md)
