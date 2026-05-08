# ExportResults Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~ExportResults`

Saves interference detection results to a file.
Saves interference detection results to a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ExportResults( _
   ByVal FileName As System.String, _
   ByVal IncludeThumbnail As System.Boolean _
) As System.Boolean
```

```

Dim instance As IInterferenceDetectionMgr
Dim FileName As System.String
Dim IncludeThumbnail As System.Boolean
Dim value As System.Boolean
 
value = instance.ExportResults(FileName, IncludeThumbnail)
```

```

System.bool ExportResults( 
   System.string FileName,
   System.bool IncludeThumbnail
)
```

```

System.bool ExportResults( 
   System.String^ FileName,
   System.bool IncludeThumbnail
) 
```

#### Parameters

*FileName*
:   Full path name of the file (**\*.xlsx** or **\*.csv**) (see **Remarks**)

*IncludeThumbnail*
:   True to include thumbnail images of interfering components in the Microsoft Excel results, false to not (see **Remarks**)

#### Return Value

True if the export is successful, false if not

Remarks

This method corresponds to the **Save Results** button in the Interference Detection PropertyManager.

Filename is a Microsoft Excel file or a **\*.csv** file that contains the information presented in the Results list box of the Interference Detection PropertyManager:

| A | B | C | D | E | F | G |
| --- | --- | --- | --- | --- | --- | --- |
| Interference ID | Interference Preview | Interference volume (mm^3) | Component 1 name | Component 2 name | Component 1 full reference | Component 2 full reference |

IncludeThumbnail is only valid if Filename is a Microsoft Excel file.

If IncludeThumbnail is true, then:

- A thumbnail is created in each row of Column B (Interference Preview).
- Each thumbnail has:
  - 128X128 pixel resolution
  - White background
  - Isometric orientation

Example

[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)  
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)  
[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.md)  
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.md)
