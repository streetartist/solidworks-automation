# GetWitnessEntitiesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWitnessEntitiesCount`

Gets the number of virtual sharp witness lines in this drawing view.
Gets the number of virtual sharp witness lines in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWitnessEntitiesCount( _
   ByRef Size As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer
 
value = instance.GetWitnessEntitiesCount(Size)
```

```

System.int GetWitnessEntitiesCount( 
   out System.int Size
)
```

```

System.int GetWitnessEntitiesCount( 
   [Out] System.int Size
) 
```

#### Parameters

*Size*
:   Size of the virtual sharp witness line data array (see **Remarks**)

#### Return Value

Number of virtual sharp witness lines in this drawing view

Remarks

Call this method to get the sizes of the arrays returned by [IView::GetWitnessGeomInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWitnessGeomInfo.md) and [IView::IGetWitnessGeomInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWitnessGeomInfo.md).

Example

[Get Virtual Sharp Witness Line Data (VBA)](Get_Virtual_Sharp_Witness_Line_Data_Example_VB.htm)  
[Get Virtual Sharp Witness Line Data (VB.NET)](Get_Virtual_Sharp_Witness_Line_Data_Example_VBNET.htm)  
[Get Virtual Sharp Witness Line Data (C#)](Get_Virtual_Sharp_Witness_Line_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
