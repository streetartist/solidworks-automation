# SetLevels Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~SetLevels`

Sets the levels-related information for importing and IGES file.
Sets the levels-related information for importing and IGES file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLevels( _
   ByVal All As System.Boolean, _
   ByVal Only As System.Object _
) As System.Boolean
```

```

Dim instance As IImportIgesData
Dim All As System.Boolean
Dim Only As System.Object
Dim value As System.Boolean
 
value = instance.SetLevels(All, Only)
```

```

System.bool SetLevels( 
   System.bool All,
   System.object Only
)
```

```

System.bool SetLevels( 
   System.bool All,
   System.Object^ Only
) 
```

#### Parameters

*All*
:   True to process all IGES levels, false to not

*Only*
:   If All is false, then specify either a long or integer, or an array of longs or integers, indicating the levels to process

#### Return Value

True if  the levels-related information is set, false if not

Example

[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.md)  
[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.md)  
[IImportIgesData::IncludeAllLevels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeAllLevels.md)  
[IImportIgesData::IncludeOnlyLevels Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~IncludeOnlyLevels.md)  
[IImportIgesData::ProcessByLevel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData~ProcessByLevel.md)
