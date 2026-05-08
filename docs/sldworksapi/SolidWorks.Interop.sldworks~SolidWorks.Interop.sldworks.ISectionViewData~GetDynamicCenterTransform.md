# GetDynamicCenterTransform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetDynamicCenterTransform`

Gets the translation between the center of the model and the plane in the specified section in this section view.
Gets the translation between the center of the model and the plane in the specified section in this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDynamicCenterTransform( _
   ByVal Index As System.Integer _
) As MathTransform
```

```

Dim instance As ISectionViewData
Dim Index As System.Integer
Dim value As MathTransform
 
value = instance.GetDynamicCenterTransform(Index)
```

```

MathTransform GetDynamicCenterTransform( 
   System.int Index
)
```

```

MathTransform^ GetDynamicCenterTransform( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Section (see **Remarks**)

#### Return Value

[Translation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) between the center of the model and the plane in the section specified for Index

Remarks

This method is only valid for section views having more than one section. Specify:

- 1 for Section 1
- 2 for Section 2
- 3 for Section 3

If the section view contains only one section and you specify 1 for Index, then this method returns Nothing or null.

Example

[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)  
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)  
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)  
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.md)
