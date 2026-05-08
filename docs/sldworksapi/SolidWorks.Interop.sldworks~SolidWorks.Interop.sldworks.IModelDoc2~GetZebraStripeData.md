# GetZebraStripeData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetZebraStripeData`

Gets zebra line data.
Gets zebra line data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetZebraStripeData( _
   ByRef Size As System.Double, _
   ByRef Ratio As System.Double, _
   ByRef Color1 As System.Integer, _
   ByRef Color2 As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Size As System.Double
Dim Ratio As System.Double
Dim Color1 As System.Integer
Dim Color2 As System.Integer
 
instance.GetZebraStripeData(Size, Ratio, Color1, Color2)
```

```

void GetZebraStripeData( 
   out System.double Size,
   out System.double Ratio,
   out System.int Color1,
   out System.int Color2
)
```

```

void GetZebraStripeData( 
   [Out] System.double Size,
   [Out] System.double Ratio,
   [Out] System.int Color1,
   [Out] System.int Color2
) 
```

#### Parameters

*Size*
:   Number of stripes

*Ratio*
:   Width of the stripes

*Color1*
:   First color in zebra stripe design

*Color2*
:   Second color in zebra stripe design

#### Return Value

Remarks

The size parameter is inversely related; a large size value generates lots of small stripes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SetZebraStripeData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetZebraStripeData.md)  
[IModelView::DisplayZebraStripes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayZebraStripes.md)
