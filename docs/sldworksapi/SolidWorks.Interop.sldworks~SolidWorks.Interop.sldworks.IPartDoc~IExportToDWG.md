# IExportToDWG Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IExportToDWG`

Obsolete. Superseded by IPartDoc::IExportToDWG2.
Obsolete. Superseded by [IPartDoc::IExportToDWG2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IExportToDWG2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IExportToDWG( _
   ByVal FilePath As System.String, _
   ByVal ModelName As System.String, _
   ByVal Action As System.Integer, _
   ByVal ExportToSingleFile As System.Boolean, _
   ByRef Alignment As System.Double, _
   ByVal IsXDirFlipped As System.Boolean, _
   ByVal IsYDirFlipped As System.Boolean, _
   ByVal SheetMetalOptions As System.Integer, _
   ByVal ViewsCount As System.Integer, _
   ByRef Views As System.String _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim FilePath As System.String
Dim ModelName As System.String
Dim Action As System.Integer
Dim ExportToSingleFile As System.Boolean
Dim Alignment As System.Double
Dim IsXDirFlipped As System.Boolean
Dim IsYDirFlipped As System.Boolean
Dim SheetMetalOptions As System.Integer
Dim ViewsCount As System.Integer
Dim Views As System.String
Dim value As System.Boolean
 
value = instance.IExportToDWG(FilePath, ModelName, Action, ExportToSingleFile, Alignment, IsXDirFlipped, IsYDirFlipped, SheetMetalOptions, ViewsCount, Views)
```

```

System.bool IExportToDWG( 
   System.string FilePath,
   System.string ModelName,
   System.int Action,
   System.bool ExportToSingleFile,
   ref System.double Alignment,
   System.bool IsXDirFlipped,
   System.bool IsYDirFlipped,
   System.int SheetMetalOptions,
   System.int ViewsCount,
   ref System.string Views
)
```

```

System.bool IExportToDWG( 
   System.String^ FilePath,
   System.String^ ModelName,
   System.int Action,
   System.bool ExportToSingleFile,
   System.double% Alignment,
   System.bool IsXDirFlipped,
   System.bool IsYDirFlipped,
   System.int SheetMetalOptions,
   System.int ViewsCount,
   System.String^% Views
) 
```

#### Parameters

*FilePath*
:   Full path to the exported DXF/DWG file

*ModelName*
:   Full path to the active part document

*Action*
:   > 1 - export sheet metal (valid only if active document contains sheet metal)
    >
    > 2 - export selected faces or loops
    >
    > 3 - export annotation views

*ExportToSingleFile*
:   True to save as one file; false to save in separate files

*Alignment*
:   Array of twelve double values that contain information related to output alignment:

    > Array[0], Array[1], Array[2] - XYZ coordinates of new origin
    >
    > Array[3], Array[4], Array[5] - coordinates of new x direction vector
    >
    > Array[6], Array[7], Array[8] - coordinates of new y direction vector
    >
    > Array[9], Array[10], Array[11] - coordinates of the vector that is normal to the selected faces or loops

    The last three elements of the array are valid only if Action = 2

*IsXDirFlipped*
:   True to flip the x direction; false otherwise

*IsYDirFlipped*
:   True to flip the y direction; false otherwise

*SheetMetalOptions*
:   [Bitmask](sldworksapiprogguide.chm::/OVERVIEW/Bitmasks.htm) that contains sheet metal export options; valid only if Action = 1:

    The bitmask is {7 6 5 4 3 2 1}, where each bit is either 0 or 1 as follows:

    > Bit #1: 1 to export geometry; 0 to not
    >
    > Bit #2: 1 to include hidden edges; 0 to not
    >
    > Bit #3: 1 to export bend lines; 0 to not
    >
    > Bit #4: 1 to include sketches; 0 to not
    >
    > Bit #5: 1 to merge coplanar faces; 0 to not
    >
    > Bit #6: 1 to export library features; 0 to not
    >
    > Bit #7: 1 to export forming tools; 0 to not

    Example

    If you want to export flat pattern geometry, bend lines, and sketches, then Bits 1, 3, and 4 are 1, the bitmask is 0001101, and you need to set SheetMetalOptions = 2^0 + 2^2 + 2^3 = 1 + 4 + 8 = 13.

*ViewsCount*
:   Count of annotation views to export; valid only if Action = 3

*Views*
:   Array of annotation view names to export; valid only if Action = 3

#### Return Value

True if export is successful; false otherwise

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ExportToDWG Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ExportToDWG.md)
