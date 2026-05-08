# SetZebraStripeData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetZebraStripeData`

Sets the zebra-line data.
Sets the zebra-line data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetZebraStripeData( _
   ByVal Size As System.Double, _
   ByVal Ratio As System.Double, _
   ByVal Color1 As System.Integer, _
   ByVal Color2 As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim Size As System.Double
Dim Ratio As System.Double
Dim Color1 As System.Integer
Dim Color2 As System.Integer
 
instance.SetZebraStripeData(Size, Ratio, Color1, Color2)
```

```

void SetZebraStripeData( 
   System.double Size,
   System.double Ratio,
   System.int Color1,
   System.int Color2
)
```

```

void SetZebraStripeData( 
   System.double Size,
   System.double Ratio,
   System.int Color1,
   System.int Color2
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

Remarks

The Size parameter is inversely related; a large size value generates lots of small stripes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetZebraStripeData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetZebraStripeData.md)  
[IModelView::DisplayZebraStripes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayZebraStripes.md)
