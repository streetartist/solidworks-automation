# ISheet Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet`

Allows access to a sheet and objects on the sheet such as BOM tables.
Allows access to a sheet and objects on the sheet such as [BOM tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISheet 
```

```

Dim instance As ISheet
```

```

public interface ISheet 
```

```

public interface class ISheet 
```

Remarks

A drawing document can consist of one or more sheets. Each sheet typically contains one or more [drawing views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md). Each drawing view is an oriented snapshot of a particular SOLIDWORKS model and a particular [configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md) of the model.

Example

[Get Sheet Properties and Insert Object (C++)](Get_Sheet_Properties_and_Insert_Object_Example_CPlusPlus_COM.htm)  
[Copy and Paste Drawing Sheet (C#)](Copy_and_Paste_Drawing_Sheet_Example_CSharp.htm)  
[Copy and Paste Drawing Sheet (VB.NET)](Copy_and_Paste_Drawing_Sheet_Example_VBNET.htm)  
[Copy and Paste Drawing Sheet (VBA)](Copy_and_Paste_Drawing_Sheet_Example_VB.htm)  
[Get and Set Sheet Properties (VBA)](Get_and_Set_Sheet_Properties_Example_VB.htm)  
[Activate Each View on Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)  
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)  
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)  
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)
