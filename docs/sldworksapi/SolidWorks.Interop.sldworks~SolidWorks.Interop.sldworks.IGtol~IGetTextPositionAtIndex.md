# IGetTextPositionAtIndex Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPositionAtIndex`

Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center).
Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTextPositionAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IGtol
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetTextPositionAtIndex(Index)
```

```

System.double IGetTextPositionAtIndex( 
   System.int Index
)
```

```

System.double IGetTextPositionAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0-based index of the piece of text

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is the following array of doubles:

[ textPtX, textPtY, textPtZ ]

where the text position values are offset values from the origin of this [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md) object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetTextAngleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextAngleAtIndex.md)  
[IGtol::GetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextAtIndex.md)  
[IGtol::GetTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextCount.md)  
[IGtol::GetTextFont Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextFont.md)  
[IGtol::GetTextHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextHeightAtIndex.md)  
[IGtol::GetTextInvertAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextInvertAtIndex.md)  
[IGtol::GetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextPoint.md)  
[IGtol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextRefPositionAtIndex.md)  
[IGtol::IGetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPoint.md)
