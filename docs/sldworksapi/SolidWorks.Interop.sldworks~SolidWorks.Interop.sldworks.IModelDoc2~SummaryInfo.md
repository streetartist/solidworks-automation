# SummaryInfo Property (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SummaryInfo`

Gets or sets file summary information for the SOLIDWORKS document.
Gets or sets file summary information for the SOLIDWORKS document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SummaryInfo( _
   ByVal FieldId As System.Integer _
) As System.String
```

```

Dim instance As IModelDoc2
Dim FieldId As System.Integer
Dim value As System.String
 
instance.SummaryInfo(FieldId) = value
 
value = instance.SummaryInfo(FieldId)
```

```

System.string SummaryInfo( 
   System.int FieldId
) {get; set;}
```

```

property System.String^ SummaryInfo {
   System.String^ get(System.int FieldId);
   void set (System.int FieldId, System.String^ value);
}
```

#### Parameters

*FieldId*
:   Identifier for field as defined in [swSummInfoField\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSummInfoField_e.html)

#### Property Value

Text in field

Remarks

In line with Microsoft recommendations for OLE support, the file summary information for SOLIDWORKS documents is written as an OLE property set into a stream named "\005Summary Information" off the root storage of the SOLIDWORKS document's compound file.

NOTES:

- MFC does not currently provide classes that manage summary information. However, the DRAWCLI application shipped with Visual C++ does include a sample implementation, in the form of the class CSummInfo, which you can use as an example when implementing your own. This class is used by the document class CDrawDoc. DRAWCLI also includes property pages for displaying and modifying Summary Information.
- Some dates are localized.

> Option Explicit
>
> Sub main()
>
>     Dim swApp           As SldWorks.SldWorks
>
>     Dim swModel         As SldWorks.ModelDoc2
>
>     Dim Text1           As String
>
>     Dim Text2           As String
>
>     Dim Text3           As String
>
>     Dim Text4           As String
>
>     Set swApp = CreateObject("SldWorks.Application")
>
>     Set swModel = swApp.ActiveDoc
>
>     
>
>     ' All of these date strings will be localized according to
>
>     ' the current regional settings
>
>     
>
>     ' These two dates (day, month, and year)
>
>     ' will be in numeric format and localized
>
>     Text1 = swModel.SummaryInfo(swSumInfoCreateDate)
>
>     Text2 = swModel.SummaryInfo(swSumInfoSaveDate)
>
>     
>
>     ' These two dates will be the same as displayed in the
>
>     ' File, Properties menu in text format
>
>     Text3 = swModel.SummaryInfo(swSumInfoCreateDate2)
>
>     Text4 = swModel.SummaryInfo(swSumInfoSaveDate2)
>
>     
>
>     Debug.Print "CreateDate = " + Text1
>
>     Debug.Print "SaveDate = " + Text2
>
>     Debug.Print "CreateDate2 = " + Text3
>
>     Debug.Print "SaveDate2 = " + Text4
>
> End Sub

Example

[Get File Summary Information (VBA)](Get_File_Summary_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::FileSummaryInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FileSummaryInfo.md)
