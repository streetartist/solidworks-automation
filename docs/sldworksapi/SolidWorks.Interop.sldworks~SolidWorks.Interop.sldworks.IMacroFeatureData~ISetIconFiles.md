# ISetIconFiles Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetIconFiles`

Sets the file names for the icons for this macro feature.
Sets the file names for the icons for this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetIconFiles( _
   ByVal IconCount As System.Integer, _
   ByRef IconFiles As System.String _
) 
```

```

Dim instance As IMacroFeatureData
Dim IconCount As System.Integer
Dim IconFiles As System.String
 
instance.ISetIconFiles(IconCount, IconFiles)
```

```

void ISetIconFiles( 
   System.int IconCount,
   ref System.string IconFiles
)
```

```

void ISetIconFiles( 
   System.int IconCount,
   System.String^% IconFiles
) 
```

#### Parameters

*IconCount*
:   Number of files for the icons

*IconFiles*
:   - in-process, unmanaged C++: Pointer to an array of the file names for the icons (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The array of the file names for IconFiles can contain either three or nine strings.

| Number of strings in array | Types of images in this order | Image format and sizes |
| --- | --- | --- |
| Three | 1. Regular 2. Suppressed 3. Highlighted | - Windows bitmap (**\*.bmp**) format - 16 pixels wide X 18 pixels high |
| Nine  **NOTES:**   - This size array is only valid for macro features created in parts, assemblies, and drawings in SOLIDWORKS 2017 and later. - SOLIDWORKS displays the appropriate images based on the current DPI setting of the display device. | 1. Regular small 2. Suppressed small 3. Highlighted small 4. Regular medium 5. Suppressed medium 6. Highlighted medium 7. Regular large 8. Suppressed large 9. Highlighted large | - Windows bitmap (**\*.bmp**) format - Recommended sizes are:   - Small: 20 pixels wide X 20 pixels high   - Medium: 32 pixels wide X 32 pixels high   - Large: 40 pixels wide X 40 pixels high |

You can specify either the full path name or just the file name for the strings; for example, c:\bitmaps\icon1.bmp or icon1.bmp.

If you change the bitmaps after inserting them with a macro feature into a SOLIDWORKS document, then the new bitmaps are not displayed until you exit and restart SOLIDWORKS.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::IGetIconFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetIconFiles.md)  
[IMacroFeatureData::IconFiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IconFiles.md)
