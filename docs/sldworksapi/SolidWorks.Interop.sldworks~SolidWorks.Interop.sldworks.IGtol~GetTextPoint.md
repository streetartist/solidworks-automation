# GetTextPoint Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextPoint`

Gets the GTol text reference point, which is the upper-left corner of the bounding rectangle.
Gets the GTol text reference point, which is the upper-left corner of the bounding rectangle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextPoint() As System.Object
```

```

Dim instance As IGtol
Dim value As System.Object
 
value = instance.GetTextPoint()
```

```

System.object GetTextPoint()
```

```

System.Object^ GetTextPoint(); 
```

#### Return Value

Array  (see **Remarks**)

Remarks

Format of return information is the following array of doubles:

*retval*[0] = X-coordinate of text reference point

*retval*[1] = Y-coordinate of text reference point

*retval*[2] = Z-coordinate of text reference point

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
[IGtol::GetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextPositionAtIndex.md)  
[IGtol::GetTextRefPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTextRefPositionAtIndex.md)  
[IGtol::IGetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPoint.md)  
[IGtol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPositionAtIndex.md)
