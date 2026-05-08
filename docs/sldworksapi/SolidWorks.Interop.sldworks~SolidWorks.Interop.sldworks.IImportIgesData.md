# IImportIgesData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData`

Allows you to specify levels and values when importing IGES data.
Allows you to specify levels and values when importing IGES data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IImportIgesData 
```

```

Dim instance As IImportIgesData
```

```

public interface IImportIgesData 
```

```

public interface class IImportIgesData 
```

Remarks

|  |  |
| --- | --- |
| **If user preference** **[swIGESImportShowLevel](ms-help://SolidWorks.Interop.swconst/SolidWorks/FileOpenOptionsGeneral.htm)** **is...** | **Then the IGES translator...** |
| True | Displays the IGES-In Surfaces, Curves, and Levels dialog to the user where the user can specify levels and values. |
| false and you retrieved IImportIgesData | Does not display the IGES-In Surfaces, Curves, and Levels dialog to the user and allows you to specify the levels and values. |
| false and you did not retrieve IImportIgesData | Does not display the IGES-In Surfaces, Curves, and Levels dialog to the user and uses the default values. |

To specify levels and values when importing IGES data:

> 1. Set the user preference swIGESImportShowLevel to false.
>
> 2. Use [ISldWorks::GetImportFileData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImportFileData.md) to get IImportIgesData.
>
> 3. Use the IImportIgesData functions to specify the levels and values.
>
> 4. Use [ISldworks::LoadFile4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.md) to load the file.

Example

[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)
