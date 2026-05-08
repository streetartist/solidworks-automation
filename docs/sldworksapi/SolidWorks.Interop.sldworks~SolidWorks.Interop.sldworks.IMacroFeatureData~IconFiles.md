# IconFiles Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IconFiles`

Gets or sets the file names for the icons for this macro feature.
Gets or sets the file names for the icons for this macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IconFiles As System.Object
```

```

Dim instance As IMacroFeatureData
Dim value As System.Object
 
instance.IconFiles = value
 
value = instance.IconFiles
```

```

System.object IconFiles {get; set;}
```

```

property System.Object^ IconFiles {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of the file names for the icons (see **Remarks**)

Remarks

The array of the file names for the icons can contain either three or nine strings.

| Number of strings in array | Types of images in this order | Image format and sizes |
| --- | --- | --- |
| Three | 1. Regular 2. Suppressed 3. Highlighted | - Windows bitmap (**\*.bmp**) format - 16 pixels wide X 18 pixels high |
| Nine  **NOTES:**   - This size array is only valid for macro features created in parts, assemblies, and drawings in SOLIDWORKS 2017 and later. - SOLIDWORKS displays the appropriate images based on the current DPI setting of the display device. | 1. Regular small 2. Suppressed small 3. Highlighted small 4. Regular medium 5. Suppressed medium 6. Highlighted medium 7. Regular large 8. Suppressed large 9. Highlighted large | - Windows bitmap (**\*.bmp**) format - Recommended sizes are:   - Small: 20 pixels wide X 20 pixels high   - Medium: 32 pixels wide X 32 pixels high   - Large: 40 pixels wide X 40 pixels high |

You can specify either the full path name or just the file name for the strings; for example, c:\bitmaps\icon1.bmp or icon1.bmp.

If you change the bitmaps after inserting them with a macro feature into a SOLIDWORKS document, then the new bitmaps are not displayed until you exit and restart SOLIDWORKS.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetIconFileCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIconFileCount.md)  
[IMacroFeatureData::IGetIconFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetIconFiles.md)  
[IMacroFeatureData::ISetIconFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetIconFiles.md)
